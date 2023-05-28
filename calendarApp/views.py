from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.conf import settings
secrets = settings.API_SECRET_FILE


scopes=['https://www.googleapis.com/auth/calendar']

class GoogleCalendarInitView(APIView):
    def get(self,request):
        try:
            flow = InstalledAppFlow.from_client_secrets_file(secrets,scopes=scopes)
            flow.redirect_uri = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
            auth_url, state = flow.authorization_url(access_type='offline',prompt='consent')
            request.session['google_auth_state'] = state
            return redirect(auth_url)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        if 'google_auth_state' not in request.session or request.GET.get('state') != request.session['google_auth_state']:
            return Response({'error': 'Invalid state parameter'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            flow = InstalledAppFlow.from_client_secrets_file(secrets,scopes=scopes)
            flow.redirect_uri = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
            flow.fetch_token(authorization_response=request.build_absolute_uri())

            if not flow.credentials.valid:
                if flow.credentials.expired and flow.credentials.refresh_token:
                    flow.credentials.refresh(Request())
            
            service = build('calendar', 'v3', credentials=flow.credentials, static_discovery=False)
            events_result = service.events().list(calendarId='primary').execute()
            events = events_result.get('items', [])

            if not events:
                return Response({'error': 'No events found'}, status=status.HTTP_404_NOT_FOUND)

            return Response({'events': events},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
