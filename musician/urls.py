from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

# router = routers.DefaultRouter()
# router.register("musicians", MusicianViewSet)

musician_list = MusicianViewSet.as_view(
    actions={"get": "list", "post": "create"})
musician_detail = MusicianViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)


urlpatterns = [
    # path("", include(router.urls))
    path("musicians/", musician_list, name="manage-list"),
    path(
        "musicians/<int:pk>/",
        musician_detail,
        name="manage-detail"
    ),
]

app_name = "musician"
