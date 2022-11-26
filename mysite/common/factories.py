from factory import Sequence, SubFactory, post_generation
from factory.django import DjangoModelFactory
from htmx_fragments.models import Image
from taggit.models import Tag
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Sequence(lambda n: "user-email-{0}@domain.com.au".format(n))
    first_name = Sequence(lambda n: "Emilie {0}".format(n))
    last_name = Sequence(lambda n: "Doe {0}".format(n))
    

    # I could use 'password = make_password()', but I would have to use it every time I add the password parameter to this factory in tests.
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        password = kwargs.pop("password", None)
        obj = super(UserFactory, cls)._create(model_class, *args, **kwargs)
        # ensure the raw password gets set after the initial save
        obj.set_password(password)
        obj.save()
        return obj


class StaffAdminFactory(UserFactory):
    is_active = True
    is_staff = True


class SuperuserFactory(StaffAdminFactory):
    is_superuser = True


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    title = Sequence(lambda n: "name {0}".format(n))


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = Sequence(lambda n: f"Tag {n}")
    slug = Sequence(lambda n: f"tag-{n}")

