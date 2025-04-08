from django.db.models import Q
from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    """
    Fayl va kataloglar uchun CRUD API.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # 🔎 3 ta kalit so‘z bo‘yicha qidirish
    def get_queryset(self):
        queryset = File.objects.all()
        search_terms = self.request.query_params.getlist('q', [])  # ✅ Default bo'sh ro'yxat

        if search_terms:
            query = Q()
            for term in search_terms[:3]:  # ✅ Faqat 3 ta kalit so‘z ishlatiladi
                if term.strip():  # ✅ Bo'sh stringlarni olib tashlash
                    query |= Q(name__icontains=term) | Q(absolute_path__icontains=term)
            queryset = queryset.filter(query)

        # 📌 Tartiblash: ?sort=name (yoki ?sort=-size)
        sort_param = self.request.query_params.get('sort', 'name')  # ✅ Default: 'name'
        allowed_sort_fields = ['name', 'size', '-name', '-size']  # ✅ Ruxsat berilgan maydonlar

        if sort_param in allowed_sort_fields:
            queryset = queryset.order_by(sort_param)  # ✅ Xavfsiz tartiblash
        else:
            queryset = queryset.order_by('name')  # ✅ Default tartiblash

        return queryset

