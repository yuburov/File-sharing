from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from api_v1.serializers import UserSerializer
from webapp.models import File


class UserProvideAccessView(APIView):
    def patch(self, request, pk):
        file_pk = self.kwargs['pk']
        file = get_object_or_404(File, pk=file_pk)
        if request.user == file.author or request.user.has_perm('webapp.change_file'):
            user_name = request.data['user_name'].strip()
            try:
                user = User.objects.get(username=user_name)
                if user in file.private_users.all():
                    return JsonResponse({'message': 'Данный пользователь уже существует'}, status=400)
                file.private_users.add(user)
                serializer = UserSerializer(user)
                return JsonResponse(data=serializer.data)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Пользователь не найден'}, status=404)
        else:
            return JsonResponse({'message': 'Доступ ограничен'}, status=403)

class DepriveUserAccessView(APIView):
    def patch(self, request, pk):
        file_pk = self.kwargs['pk']
        file = get_object_or_404(File, pk=file_pk)
        if request.user == file.author or request.user.has_perm('webapp.change_file'):
           serializer = UserSerializer(data=request.data, partial=True)
           if serializer.is_valid():
               user_pk = request.data['id']
               user = get_object_or_404(User, pk=user_pk)
               file.private_users.remove(user)
           return JsonResponse(data=request.data)
        else:
            JsonResponse({'message': 'Доступ ограничен'}, status=403)




