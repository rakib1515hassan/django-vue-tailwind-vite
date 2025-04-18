# Generated by Django 4.2.6 on 2024-09-19 17:20

import apps.users.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')], verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801XXXXXXXXX'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(2, message='First name must be at least 2 characters long.')], verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(2, message='First name must be at least 2 characters long.')], verbose_name='Last name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'others')], max_length=10, null=True, verbose_name='Gender')),
                ('religion', models.CharField(blank=True, choices=[('Islam', 'islam'), ('Hindu ', 'hindu'), ('Christian', 'christian'), ('Buddhist', 'buddhist'), ('Others', 'others')], max_length=20, null=True, verbose_name='Religion')),
                ('dob', models.DateField(blank=True, null=True, validators=[apps.users.validators.DateOfBirthValidator], verbose_name='Date of birth')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Users/ProfileImage/', validators=[apps.users.validators.ImageValidator], verbose_name='Profile Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_email_verified', models.BooleanField(default=False, verbose_name='Email Verification')),
                ('email_verified_at', models.DateTimeField(blank=True, null=True, verbose_name='Email Verification Time')),
                ('is_phone_verified', models.BooleanField(default=False, verbose_name='Phone Verification')),
                ('phone_verified_at', models.DateTimeField(blank=True, null=True, verbose_name='Phone Verification Time')),
                ('auth_provider', models.CharField(choices=[('Local', 'local'), ('Google', 'google'), ('Twitter', 'twitter'), ('Facebook', 'facebook'), ('Instagram', 'instagram')], default='Local', max_length=20, verbose_name='Authentication With')),
                ('fcm_device_token', models.TextField(blank=True, null=True, verbose_name='Device Token')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('otp', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000, message='OTP must be a 6-digit number.'), django.core.validators.MaxValueValidator(999999, message='OTP must be a 6-digit number.')], verbose_name='OTP Code')),
                ('token', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Token must be a valid 64-character string.', regex='^[A-Za-z0-9-_]{64}$')], verbose_name='Token')),
                ('is_used', models.BooleanField(default=False, verbose_name='Is Used')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User OTP',
                'verbose_name_plural': 'User OTPs',
            },
        ),
    ]
