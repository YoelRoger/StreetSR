from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, SubmitField, SelectField, HiddenField
from wtforms import validators
from wtforms.fields import DateField as DateTimeField

class ReportEdit(FlaskForm):
    # Definicion de campo Float
    depth = FloatField(
        label="Longitude",
        validators=[validators.DataRequired(message="This field should be an integer")])

    # Definicion de campo Float
    magnitude = FloatField(
        label="Latitude",
        validators=[validators.DataRequired(message="This field should be a decimal value")])

class ReportsFilter(FlaskForm):

    userId = SelectField(
        label="User name",
        validators=[validators.optional()],
        coerce=int)

    from_datetime = DateTimeField(
        label="Since date", format='%Y-%m-%dT%H:%M',
        validators=[validators.optional()]
    )

    to_datetime = DateTimeField(
        label="Until date", format='%Y-%m-%dT%H:%M',
        validators=[validators.optional()]
    )

    sort_by = HiddenField()

    per_page = IntegerField(
        validators=[validators.optional()]
    )

    submit = SubmitField(
        label="Filter",
    )