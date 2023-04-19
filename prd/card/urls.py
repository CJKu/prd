from django.urls import path

from card.views import UserList, PublicCardUpdateView, PublicCardDetail, PublicCardCreateView

app_name = 'card'
urlpatterns = [
    # post views
    path('', UserList.as_view()),
    path('<int:pk>', PublicCardDetail.as_view()),
    path('public_card_create', PublicCardCreateView.as_view(), name='public_card_create'),
    path('public_card_update/<int:pk>', PublicCardUpdateView.as_view(), name='public_card_update'),
]
