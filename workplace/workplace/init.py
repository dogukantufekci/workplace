from people.models import Person
from users.models import User
from workplaces.models import Workplace

workplace = Workplace.objects.create(identifier='creco', recovery_email='dogukan@creco.co')
person = Person.objects.create(workplace=workplace, first_name='Dogukan', last_name='Tufekci')
user = User.objects.create_superuser(workplace=workplace, person=person, identifier='dogukan', password='dogukan')