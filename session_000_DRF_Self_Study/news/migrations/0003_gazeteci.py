# Generated by Django 4.1.1 on 2022-09-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_makale_yazar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gazeteci",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isim", models.CharField(max_length=120)),
                ("soyisim", models.CharField(max_length=120)),
                ("biyografi", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
