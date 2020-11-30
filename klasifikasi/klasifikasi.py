from ._klasifikasi_model import KlasifikasiModel
from ._settings import BASE_URL
class Klasifikasi:
  def __init__(self, creds, url = BASE_URL):
    if (not isinstance(creds, list)):
      raise Exception('Creds must be a list of dict contain client_id & client_secret')
    
    self.__model_mapping = {}
    for data in creds:
      if (not isinstance(data, dict) or data.get('client_id') is None or data.get('client_secret') is None):
        raise Exception('Creds must be a list of dict contain client_id & client_secret')
      
      self.__model_mapping[data.get('client_id')] = KlasifikasiModel(data.get('client_id'), data.get('client_secret'), url)
      
    
  def get_models(self):
    return self.__model_mapping