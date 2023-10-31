import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


# Create queries within functions
# def create_pet(name, species):
#     Pet.objects.create(name=name, species=species)
#     return f"{name} is a very cute {species}!"
#
# def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
#     Artifact.objects.create(name = name, origin=origin, age=age, description=description, is_magical=is_magical)
#     return f"The artifact {name} is {age} years old!"
#
# def delete_all_artifacts():
#     Artifact.objects.all().delete()
#
# # def add_locations(name, region, population, description, is_capital):
# #     Location.objects.create(name=name, region=region, population=population, description=description, is_capital=is_capital)
# #     return 'location added'
#
# def show_all_locations():
#     list = []
#
#     for location in Location.objects.all().order_by('-id'):
#         list.append(f"{location.name} has a population of {location.population}!")
#
#     return "\n".join(list)
#
# def new_capital():
#     first_location = Location.objects.first()
#     first_location.is_capital = True
#     first_location.save()
#
# def get_capitals():
#     return Location.objects.filter(is_capital=True).values('name')
#
# def delete_first_location():
#     Location.objects.first().delete()
#
#
# def populate_cars(model, year, color, price):
#     Car.objects.create(model=model, year=year, color=color, price=price)
#
# def apply_discount():
#     for car in Car.objects.all():
#         percentage_off = sum(int(x) for x in str(car.year)) / 100
#         car.price_with_discount = float(car.price) - float(car.price) * percentage_off
#         car.save()
#
# def get_recent_cars():
#     return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')
#
# def delete_last_car():
#     Car.objects.last().delete()
#
# def populate_tasks(title, description, due_date, is_finished):
#     Task.objects.create(title=title, description=description, due_date=due_date, is_finished=is_finished)
#
# def show_unfinished_tasks():
#     unfinished_tasks = Task.objects.filter(is_finished=False)
#     tasks = []
#     for task in unfinished_tasks:
#         tasks.append(f"Task - {task.title} needs to be done until {task.due_date}!")
#     return '\n'.join(tasks)
#
# def complete_odd_tasks():
#     for task in Task.objects.all():
#         if task.id % 2 != 0:
#             task.is_finished = True
#             task.save()
#
# def encode_and_replace(text: str, task_title: str):
#     decoded_text = ''.join(chr(ord(x) - 3) for x in text)
#     tasks_with_title = Task.objects.filter(title=task_title)
#     for task in tasks_with_title:
#         task.description = decoded_text
#         task.save()
#
# # def populate_rooms(room_number, room_type, capacity, amenities, price_per_night):
# #     HotelRoom.objects.create(room_number=room_number, room_type=room_type, capacity=capacity, amenities=amenities, price_per_night=price_per_night)

def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_id_deluxe_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_id_deluxe_rooms.append(str(room))

    return '\n'.join(even_id_deluxe_rooms)

def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()


