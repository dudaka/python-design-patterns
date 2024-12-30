class QueryBuilder:
  def __init__(self):
    self._query = ""

  def select(self, columns):
    self._query += f'SELEECT {", ".join(columns)} '
    return self
  
  def from_(self, table):
    self._query += f'FROM {table} '
    return self
  
  def where(self, conditions):
    self._query += f'WHERE {", ".join(conditions)} '
    return self
  
  def order_by(self, columns):
    self._query += f'ORDER BY {", ".join(columns)} '
    return self
  
  def group_by(self, columns):
    self._query += f'GROUP BY {", ".join(columns)} '
    return self
  
  def limit(self, limit):
    self._query += f'LIMIT {limit} '
    return self
  
  def get_query(self):
    return self._query
  

if __name__ == "__main__":
  query_builder = QueryBuilder()

  query = query_builder.select(['name', 'age']).from_('users').where(['age > 18']).order_by(['name']).group_by(['name']).limit(10).get_query()

  print(query)