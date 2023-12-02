# Generated by Django 4.2.7 on 2023-12-02 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoGuitarra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('imagen', models.ImageField(blank=True, help_text='Imagen del usuario', null=True, upload_to='usuarios')),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.ciudad')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pais')),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='SubModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Guitarra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('ano_fabricacion', models.IntegerField(blank=True, help_text='Año de fabricación de la guitarra', null=True)),
                ('tipo_cuerpo', models.CharField(blank=True, help_text='Tipo de cuerpo de la guitarra', max_length=50, null=True)),
                ('material_diapason', models.CharField(blank=True, help_text='Material del diapasón de la guitarra', max_length=50, null=True)),
                ('numero_trastes', models.IntegerField(blank=True, help_text='Número de trastes de la guitarra', null=True)),
                ('color', models.CharField(blank=True, help_text='Color de la guitarra', max_length=50, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=2, help_text='Peso de la guitarra', max_digits=5, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='Imagen de la guitarra', null=True, upload_to='guitarras')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.marca')),
                ('sub_modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.submodelo', verbose_name='Submodelo')),
                ('tipo_guitarra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.tipoguitarra')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pais'),
        ),
    ]