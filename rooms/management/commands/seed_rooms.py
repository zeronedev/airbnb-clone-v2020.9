import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command  creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number", 2)
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenityes = room_models.Amenity.objects.all()  # 편의시설
        facilities = room_models.Facility.objects.all()  # 설비
        rules = room_models.HouseRule.objects.all()  # 규칙
        print(amenityes, facilities, rules)
        print(created_clean)  # flatten 간결한 리스트로 표시 - [[]] 를 [] 로 변환
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            print(room)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                    room=room,
                )
            for a in amenityes:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)  # 다대다에서 추가하는 방법
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)
                    # print(magic_number, r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
