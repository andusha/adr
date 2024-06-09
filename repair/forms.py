from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import Length, DataRequired, Regexp

phone_regex = r'^(\+7|8)[0-9][0-9]{9}$'

class StatementForm(FlaskForm):
    name = StringField(
        "ФИО: ",
        validators=[
            DataRequired(),
            Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")
        ],
        render_kw={"placeholder": "ФИО"},
    )
    phone = StringField(
        "Phone: ",
        validators=[
            DataRequired(),
            Regexp(phone_regex, message="Некорректный формат номера телефона"),
        ],
        render_kw={"placeholder": "Телефон"},
    )
    comm = TextAreaField(
        "Опишите проблему",
        render_kw={"placeholder": "Комментарий"},
    )

    submit = SubmitField("Оставить заявку")
