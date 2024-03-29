# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import CreationDateTimeField


# BusinessPartner table 안 생김
class BusinessPartner(User):
    """
    업체(추천 서비스를 직접 사용하는)
    proxy 모델로 만들어서 django의  auth_user 테이블을 그대로 사용한다.
    """

    class Meta:
        proxy = True


class Movie(models.Model):
    """
    영화 데이터
    movie_pk PrimaryKey
    title 제목
    genre 장르
    description 줄거리
    rate 평점
    votes 투표수
    running_time 영화 시간(분)
    created_at 이 객체가 생성된 시간
    director 감독
    movie_owner 이 영화를 가지고 있는 업체 (ManyToManyField 로 through 클래스로 구현)

    """
    # 이 값이 영화가 계속 추가되면 달라져야하는데..?
    movie_pk: str = models.CharField(
        help_text="영화의 PrimaryKey",
        max_length=64,
        null=False,
        primary_key=True
    )

    title: str = models.CharField(
        help_text="영화 제목",
        max_length=256,
        null=False,
    )

    genre: str = models.CharField(
        help_text="영화 장르, ',' 를 기준으로 분류",
        max_length=256,
        default="genre"
    )

    description: str = models.CharField(
        help_text="영화 줄거리",
        max_length=256,
        null=True,
        default="Lorem ipsum dolor sit amet, "
                "consectetur adipiscing elit. "
                "Nam eget consequat eros, a lacinia turpis. "
                "Phasellus faucibus commodo diam",
    )

    rate: float = models.FloatField(
        help_text="영화 평점",
        default=0.0,
    )
    votes: int = models.IntegerField(
        help_text="퍙점 투표수",
        default=0,
    )
    running_time: int = models.IntegerField(
        help_text="영화 시간, 분을 기준으로",
        default=0,
    )

    # 생성된 날짜, 시간
    created_at: datetime = CreationDateTimeField()

    director: str = models.CharField(
        help_text="감독명, ',' 를 기준으로 분류",
        max_length=256,
        null=True,

    )

    movie_owner: BusinessPartner = models.ManyToManyField(
        BusinessPartner,
        through='BusinessPartnerMovie',
    )


class BusinessPartnerMovie(models.Model):
    """
    업체와 영화 사이의 M2M 클래스 ( 업체가 보유한 영화 )
    businessPartner 업체
    movie 영화
    """
    businessPartner: BusinessPartner = models.ForeignKey(
        BusinessPartner,
        on_delete=models.CASCADE
    )

    movie: Movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )


class Actor(models.Model):
    """
    배우 데이터
    actor_pk PrimaryKey
    name 이름
    created_at 이 객체가 생성된 시간
    movie 배우가 출연한 영화 ( M2M field  클래스로 구현)
    """
    name: str = models.CharField(
        help_text="배우 이름, ',' 를 기준으로 분류",
        max_length=256,
        null=False,
    )

    actor_pk: str = models.CharField(
        help_text="영화의 PrimaryKey",
        max_length=64,
        null=False,
        primary_key=True
    )
    created_at: datetime = CreationDateTimeField()

    movie: Movie = models.ManyToManyField(
        Movie,
        through='ActorMovie',
    )


class ActorMovie(models.Model):
    """
    배우와 영화 사이의 M2M 클래스 ( 영화에 출연한 배우)
    actor 배우
    movie 영화
    created_at 이 객체가 생성된 시간
    """
    actor: Actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE
    )

    movie: Movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    created_at: datetime = CreationDateTimeField()


class Customer(models.Model):
    """
    고객 데이터 (업체의 고객)
    gender 성별 True 남성, False 여성
    age 나이
    nickname 아이디, 닉네임
    associated_bp 소속된 업체 (FK)
    movie 고객이 평가한 영화 ( M2M field through 클래스로 구현)
    created_at 이 객체가 생성된 시간
    """
    gender: str = models.BooleanField(
        help_text="고객의 성별, True 남성, False 여성"
    )

    age: int = models.IntegerField(
        help_text="고객의 나이",
        null=False
    )

    nickname: str = models.CharField(
        help_text="업체에서의 ID",
        max_length=64,
        null=False,
    )

    associated_bp: BusinessPartner = models.ForeignKey(
        to=BusinessPartner,
        on_delete=models.CASCADE
    )

    movie: Movie = models.ManyToManyField(
        Movie,
        through='CustomerMovie',
    )

    created_at: datetime = CreationDateTimeField()


class CustomerMovie(models.Model):
    """
    고객과 영화 사이의 M2M 클래스 ( 고객이 평가한 영화 )
    customer 고객
    movie 영화
    rate 평점
    created_at 이 객체가 생성된 시간
    """
    customer: Customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    movie: Movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    rate: float = models.FloatField(
        help_text="고객의 영화에 대한 평점",
        null=False,
        default=None
    )

    created_at: datetime = CreationDateTimeField()
