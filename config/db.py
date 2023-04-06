from sqlalchemy import create_engine, MetaData

meta = MetaData()
engine = create_engine('mysql+pymysql://root:Rijin222001@localhost:3306/carbon')


conn = engine.connect()
