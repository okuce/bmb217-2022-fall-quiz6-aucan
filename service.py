"""Quiz 6
Numara:
Ad Soyad:
"""


from datetime import date
class Service:
    """Tamir servisi işlemlerini yapan sınıf"""

    """işçilik ücreti oranını ve servisin adını class variable olarak tanımlayıp, 
    ilk değerlerini giriniz. """
    workmanship_rate:float = 0.15
    service_name:str = "Osman Usta"


    """ price_list dictionary'si class variable olarak tanımlanmıştır
        üzerinde herhangi bir değişiklik yapmayınız
        yapılan işlemin ücretini hesaplamak için faydalanmalısınız.
    """
    price_list = {
        "yag":400,
        "yag_filtresi":75,
        "hava_filtresi":110,
        "polen_filtresi":60,
        "yikama":50,
        "motor_temizligi":100,
        "buji":600,
        "aku":1500,
        "balata":750,
        "disk":1600,
        "triger":1250,
    }

    def __init__(self, plate_no:str, name_surname:str, work_list:list[str]) -> None:
        """Service constructor

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str]): yapılacak iş listesi
        """
        self.plate_no = plate_no
        self.name_surname = name_surname
        self.work_list = work_list
        self.__work_price = []
        self.total = 0

    @classmethod
    def onbin(cls,plate_no:str, name_surname:str, work_list:list[str]=[]):
        """onbin bakımı için ön tanımlı iş listesine sahip constructor overload

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].

        ön tanımlı iş listesi["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """
        work_list.extend(["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"])
        return cls(plate_no,name_surname,work_list)
    
    @classmethod
    def yirmibin(cls,plate_no:str, name_surname:str, work_list:list[str]=[]):
        """yirmibin bakımı için ön tanımlı iş listesine sahip constructor overload

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].

        ön tanımlı iş listesi["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """
        work_list = ["motor_temizligi","balata","disk"]
        return cls.onbin(plate_no,name_surname,work_list)
    
    @classmethod
    def otuzbin(cls,plate_no:str, name_surname:str, work_list:list[str]=[]):
        """otuzbin bakımı için ön tanımlı iş listesine sahip constructor overload

        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].

        ön tanımlı iş listesi["triger","buji","motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """
        work_list = ["triger","buji"]
        return cls.yirmibin(plate_no,name_surname,work_list)
    
    @property
    def name_surname(self) -> str:
        """name_surname getter

        Returns:
            str: __name ve __surname gizli değişkenlerinde tutulan anonimleştirilmiş isim ve soy ismi geriye döndürür
            örnek: Ala*** Uça***
        """
        return f'{self.anonymize(self.__name)} {self.anonymize(self.__surname)}'

    @name_surname.setter
    def name_surname(self,value:str) -> None:
        """name_surname setter

        Args:
            value (str): içerisine isim ve soyisim alıyor ve __name ve __surname gizli değişkenlerine atama yapıyor.
        """
        self.__name,self.__surname = value.split()

    @classmethod
    def set_workmanship_rate(cls,workmanship_rate:float) -> None:
        """işçilik oranı class variable ını değiştiren class method

        Args:
            workmanship_rate (float): işçilik oranı
        """
        cls.workmanship_rate = workmanship_rate

    @classmethod
    def set_service_name(cls,service_name) -> None:
        """servis adı class variable nı değiştiren class method

        Args:
            service_name (_type_): servis adı 
        """
        cls.service_name = service_name

    def do_worklist(self):
        """iş listesinde yer alan her işçilik kalemi için
           önce işin fiyatını bulur
           sonra işçilik oranına göre işçilik ücretini hesaplar
           yapılan işler listesine ekler
        """
        for work in self.work_list:
            price = self.price_list[work]
            workmanship = price * self.workmanship_rate
            self.total += price + workmanship
            self.__work_price.append(f'*{work},{price}tl,{workmanship}tl')

    def print(self) -> None:
        """serviste yapılan işlerin ücret özetini ekrana basar
        format:
            20 tane -
            <plaka>-<anonimleştirilmiş isim soy isim>-<bugünkü tarih, yıl,ay,gün>
            başında * ile yapılan her bir işlemi alt alta *<work>,<price>tl,<workmanship>tl
            İşçilik Oranı: <workmanship_rate>
            Toplam: <toplam_tutar>tl
            Servis: <service_name>
            20 tane -
        """
        print('-' * 20)
        print(f'{self.plate_no}-{self.name_surname}-{date.today()}')
        for wp in self.__work_price:
            print(wp)
        print(f'İşçilik Oranı:{self.workmanship_rate}')
        print(f'Toplam:{self.total}tl')
        print(f'Servis:{self.service_name}')
        print('-' * 20)
        

    @staticmethod
    def anonymize(_in) -> str:
        """Gelen stringin ilk üç harfini alır ve 
        sonuna *** ekleyerek anonimleştirme işlemi gerçekleştirir.
        Bu bir static methoddur.

        Args:
            _in (str): gelen string

        Returns:
            str: anonimleşmiş string
        """
        _out:str = ""
        _out = _in[:3]+"***"
        return _out