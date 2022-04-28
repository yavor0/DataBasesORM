from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# mysql://root:123456y@127.0.0.1/test
engine = create_engine('sqlite://', echo=True)
Base = declarative_base()


class Position(Base):
    __tablename__ = 'positions'
    position_code = Column(String(2), primary_key=True)
    name = Column(String(30))
    # players = relationship("players")

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    num = Column(Integer, nullable=False)
    position_code = Column(String(2), ForeignKey('positions.position_code'))
    

positions = [
    Position(position_code="GK", name="Вратар"),
    Position(position_code="RB", name="Десен защитник"),
    Position(position_code="LB", name="Ляв защитник"),
    Position(position_code="CB", name="Централен защитник"),
    Position(position_code="RM", name="Десен полузащитник"),
    Position(position_code="LM", name="Ляв полузащитник"),
    Position(position_code="CM", name="Полузащитник"),
    Position(position_code="CF", name="Централен нападател")
]

players = [
    Player(name="Ivaylo Trifonov", num=1, position_code="GK"),
    Player(name="Valko Trifonov", num=2, position_code="RB"),
    Player(name="Ognyan Yanev", num=3, position_code="CB"),
    Player(name="Zahari Dragomirov", num=4, position_code="CB"),
    Player(name="Bozhidar Chilikov", num=5, position_code="LB"),
    Player(name="Timotei Zahariev", num=6, position_code="CM"),
    Player(name="Marin Valentinov", num=7, position_code="CM"),
    Player(name="Mitre Cvetkov", num=99, position_code="CF"),
    Player(name="Zlatko Genov", num=9, position_code="CF"),
    Player(name="Matey Goranov", num=10, position_code="RM"),
    Player(name="Sergei Zhivkov", num=11, position_code="LM")
]



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all(positions)
session.commit()

session.add_all(players)
session.commit()

for x in session.query(Position, Player).filter(Player.position_code == Position.position_code).all():
   print (f"{x.Player.name} : {x.Position.name}")
