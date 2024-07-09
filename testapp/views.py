from django.shortcuts import render

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Organisation, Member, Role
from .serializers import UserSerializer, OrganisationSerializer, MemberSerializer, RoleSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_object()
        org = Organisation.objects.create(name=f"{user.email}'s Organisation", status=0)
        owner_role = Role.objects.create(name="Owner", org_id=org)
        Member.objects.create(org_id=org, user_id=user, role_id=owner_role, status=0)
        return response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializer

class ResetPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class InviteMemberView(APIView):
    def post(self, request):
        pass

class DeleteMemberView(APIView):
    def delete(self, request, member_id):
        try:
            member = Member.objects.get(id=member_id)
            member.delete()
            return Response({"message": "Member deleted."}, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response({"error": "Member not found."}, status=status.HTTP_404_NOT_FOUND)

class UpdateMemberRoleView(APIView):
    def put(self, request, member_id):
        try:
            member = Member.objects.get(id=member_id)
            new_role_id = request.data.get('role_id')
            new_role = Role.objects.get(id=new_role_id)
            member.role_id = new_role
            member.save()
            return Response({"message": "Member role updated."}, status=status.HTTP_200_OK)
        except (Member.DoesNotExist, Role.DoesNotExist):
            return Response({"error": "Member or role not found."}, status=status.HTTP_404_NOT_FOUND)
