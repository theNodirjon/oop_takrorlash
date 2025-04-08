from django.db import models

class File(models.Model):
    FILE_TYPES = [('file', 'File'), ('directory', 'Directory')]

    name = models.CharField(max_length=255)  # Fayl yoki katalog nomi
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)  # Fayl yoki katalog ekanligi
    parent_directory = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_files')  # Ota katalog
    absolute_path = models.CharField(max_length=500)  # To'liq yo'l
    size = models.BigIntegerField()  # Fayl hajmi (baytlarda)
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana
    updated_at = models.DateTimeField(auto_now=True)  # O‘zgartirilgan sana

    def __str__(self):
        return self.name
