from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ResetPasswordView, InviteMemberView, DeleteMemberView, UpdateMemberRoleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-pass/', ResetPasswordView.as_view(), name='reset_password'),
    path('invite-member/', InviteMemberView.as_view(), name='invite_member'),
    path('delete-member/<int:member_id>/', DeleteMemberView.as_view(), name='delete_member'),
    path('update-role/<int:member_id>/', UpdateMemberRoleView.as_view(), name='update_member_role'),
]