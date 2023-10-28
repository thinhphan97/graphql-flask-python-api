import sys
from datetime import datetime

sys.path.append(".")

from api import db
from api.models import Post

current_date = datetime.today().date()
new_postes = []
for i in range(10):
    new_postes.append(Post(title=f"Sample {i}", description=f"Description of sample {i}", created_at=current_date))
db.create_all()
db.session.add_all(new_postes)
db.session.commit()