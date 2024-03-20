from pydantic import BaseModel, Field

class InputModel(BaseModel):
    """MyNewPiece Input"""
    in_argument_1: float = Field(
        default=1.,
        description="an argument of numeric type with default value",
    )
    in_argument_2: str = Field(
        description="a required argument of string type"
    )
    in_argument_3: bool = Field(
        description="a required argument of boolean type"
    )

class OutputModel(BaseModel):
    """MyNewPiece Output"""
    out_argument_1: str = Field(
        description="an argument of string type"
    )
    out_file_path: str = Field(
        description="The path to a file saved in a shared storage"
    )

class SecretsModel(BaseModel):
    """MyNewPiece Secrets"""
    SECRET_VAR: str = Field(
        description="Secret variable"
    )