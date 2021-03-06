# Generated by Django 2.1.1 on 2018-09-02 05:15

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180901_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='category', chained_model_field='category', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Subcategory'),
        ),
    ]
