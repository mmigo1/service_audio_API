from django.http import FileResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from pydub import AudioSegment

import os


class UserRegis(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Ваш ID': serializer.data['id'], 'Ваш токен:': serializer.data['uuid']},
                        status=status.HTTP_201_CREATED)


class AddAudio(APIView):
    def get(self, request):
        audio = Audio.objects.all()
        return Response({'audio': AudioSerializer(audio, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            user_id: int = request.data['id']
            user_token: str = request.data['token']
            user: bool = CustomUser.objects.filter(id=user_id, uuid=user_token).exists()
        except:
            return HttpResponseBadRequest('Ошибка данных', status=status.HTTP_400_BAD_REQUEST)
        if user:
            serializer = AudioSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            uuid: str = serializer.data['id']
            audio: object = Audio.objects.get(id=uuid)
            base, ext = os.path.splitext(audio.file.name)
            if ext not in ('wav', 'mp3'):
                audio = Audio.objects.get(id=uuid)
                os.remove(audio.file.path)
                audio.delete()
                return Response('Неверный тип файла', status=status.HTTP_400_BAD_REQUEST)
            AudioSegment.from_file(f'{audio.file.name}').normalize().export(base + '.mp3',
                                                                            'mp3')
            Audio.objects.filter(id=serializer.data['id']).update(file=base + '.mp3')
            url: str = f'http://localhost:8000/record?uuid={uuid}&id={user_id}'
            return Response({
                'URL для скачивания аудиозаписи': url}, status=status.HTTP_200_OK)
        else:
            return Response(['Неверно введены данные'], status=status.HTTP_400_BAD_REQUEST)


def get_audio(request):
    try:
        id: int = request.GET['id']
        uuid: str = request.GET['uuid']
    except:
        return HttpResponseBadRequest('Ошибка данных', status=status.HTTP_400_BAD_REQUEST)
    user: bool = CustomUser.objects.filter(id=id).exists()
    audio: bool = Audio.objects.filter(id=uuid).exists()
    if user and audio:
        audio: object = Audio.objects.get(id=uuid)
        filename: str = audio.file.path
        return FileResponse(open(filename, 'rb'), status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest('Ошибка данных', status=status.HTTP_400_BAD_REQUEST)
