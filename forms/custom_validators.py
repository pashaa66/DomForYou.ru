from wtforms.validators import ValidationError

def check_phone(field):
    phone_number = ''.join(field.data.split())
    if any(map(lambda symbl: symbl.isalpha(), phone_number)):
        raise ValidationError('неверный формат')
    if not phone_number.startswith('+7') and not phone_number.startswith('8'):
        raise ValidationError('неверный формат')
    if '(' in phone_number or ')' in phone_number:
        if phone_number.count('(') != phone_number.count(')'):
            raise ValidationError('неверный формат')
        if phone_number.count('(') != 1:
            raise ValidationError('неверный формат')
        if phone_number.find('(') > phone_number.find(')'):
            raise ValidationError('неверный формат')
        phone_number = phone_number.replace('(', '').replace(')', '')
    if not all(phone_number.split('-')):
        raise ValidationError('неверный формат')
    phone_number = phone_number.replace('-', '')
    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]
    if len(phone_number[1:]) != 11:
        raise ValidationError('неверное количество цифр')
    return phone_number

def FileSizeLimit(max_size_in_mb):
    max_bytes = max_size_in_mb*1024*1024

    def file_length_check(form, field):
        if len(field.data.read()) > max_bytes:
            raise ValidationError(
                f'File size is too large. Max allowed: {max_size_in_mb} MB')
        field.data.seek(0)
    return file_length_check
