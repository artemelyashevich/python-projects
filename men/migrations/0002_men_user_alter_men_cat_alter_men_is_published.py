from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("men", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="men",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="men",
            name="cat",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="men.category",
            ),
        ),
        migrations.AlterField(
            model_name="men",
            name="is_published",
            field=models.BooleanField(auto_created=True),
        ),
    ]
