import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uet_manager.settings')
    # from django.core.management import execute_from_command_line
    # if len(sys.argv) == 2 and sys.argv[1] == 'runserver':
    #     execute_from_command_line(sys.argv)
    # else:
    #     print("Mời chạy lệnh: ")
    #     print("python manage.py runserver")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
