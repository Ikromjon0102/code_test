from django.db import migrations, models
from django.utils.text import slugify

def populate_slug(apps, schema_editor):
    Theme = apps.get_model('problems', 'Theme')
    for theme in Theme.objects.all():
        theme.slug = slugify(theme.name)
        theme.save()

class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_theme_slug'),  # Ensure this matches your initial migration file
    ]

    operations = [
        migrations.RunPython(populate_slug),
    ]
