
# Init DB
docker-compose exec db /app/docker/postgres/db_init.sh

# Migrations
docker-compose exec django python3 manage.py migrate

# Admin user
docker-compose exec django python3 manage.py shell -c "from django.contrib.auth.models import User;User.objects.create_superuser('admin', 'tech@microdisseny.com', 'admin')"

# Load data
docker-compose exec django python3 manage.py load_locations data/list-ES-E17.json
