import json

class ContactManager:
    def init(self):
        self.contacts = []

    def add_contact(self, id, name, mobile, email):
        contact = {
            'id': id,
            'name': name,
            'mobile': mobile,
            'email': email
        }
        self.contacts.append(contact)

    def edit_contact(self, id, name, mobile, email):
        for contact in self.contacts:
            if contact['id'] == id:
                contact['name'] = name
                contact['mobile'] = mobile
                contact['email'] = email
                break

    def delete_contact(self, id):
        self.contacts = [contact for contact in self.contacts if contact['id'] != id]

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword in contact['name'] or keyword in contact['mobile'] or keyword in contact['email']:
                results.append(contact)
        return results

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

if __name__ == "__main__":
    contact_manager = ContactManager()
    while True:
        print("1. إضافة جهة اتصال")
        print("2. تعديل جهة اتصال")
        print("3. حذف جهة اتصال")
        print("4. عرض جهات الاتصال")
        print("5. البحث في جهات الاتصال")
        print("6. حفظ الجهات الاتصال في ملف JSON")
        print("7. تحميل الجهات الاتصال من ملف JSON")
        print("8. الخروج")

        choice = input("الرجاء اختيار الإجراء المطلوب: ")

        if choice == '1':
            id = input("ادخل معرف الجهة الاتصال: ")
            name = input("ادخل الاسم: ")
            mobile = input("ادخل رقم الجوال: ")
            email = input("ادخل البريد الإلكتروني: ")
            contact_manager.add_contact(id, name, mobile, email)
        elif choice == '2':
            id = input("ادخل معرف الجهة الاتصال للتعديل: ")
            name = input("الاسم الجديد: ")
            mobile = input("الرقم الجديد للجوال: ")
            email = input("البريد الإلكتروني الجديد: ")
            contact_manager.edit_contact(id, name, mobile, email)
        elif choice == '3':
            id = input("ادخل معرف الجهة الاتصال للحذف: ")
            contact_manager.delete_contact(id)
        elif choice == '4':
            print(contact_manager.contacts)
        elif choice == '5':
            keyword = input("ادخل كلمة البحث: ")
            results = contact_manager.search_contact(keyword)
            print(results)
        elif choice == '6':
            filename = input("ادخل اسم ملف JSON للحفظ: ")
            contact_manager.save_to_json(filename)
        elif choice == '7':
            filename = input("ادخل اسم ملف JSON للتحميل: ")
            contact_manager.load_from_json(filename)
        elif choice == '8':
            break