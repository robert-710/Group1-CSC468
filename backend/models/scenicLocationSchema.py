from marshmallow import Schema, fields, validate, post_load
from models.scenicLocation import ScenicLocation

class ScenicLocationSchema(Schema):
    location_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=128))
    description = fields.Str(validate=validate.Length(max=255))
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)

    @post_load
    def make_scenic_location(self, data, **kwargs):
        return ScenicLocation(**data)
