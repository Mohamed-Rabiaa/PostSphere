from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, email, password, **extra_fields):
        if not name:
            raise ValueError("name is missing")
        if not email:
            raise ValueError("email is missing")
        if not password:
            raise ValueError("password is missing")

        user = self.model(
            name=name,
            email = self.normalize_email(email),
            **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(name, email, password, **extra_fields)
