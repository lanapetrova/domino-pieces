from domino.base_piece import BasePiece
from .models import InputModel, SecretsModel, OutputModel
from pathlib import Path

class MyNewPiece(BasePiece):

    # Your custom function code comes in here
    def piece_function(self, input_data: InputModel, secrets_data: SecretsModel):

        # The Piece's input arguments are passed in the 'input_data' argument
        print(f"Inpu argument 1: {input_data.in_argument_1}")
        print(f"Inpu argument 2: {input_data.in_argument_2}")
        print(f"Inpu argument 3: {input_data.in_argument_3}")

        # The Piece's secrets are passed in the 'secrets_data' argument
        print(f"Secret variable: {secrets_data.SECRET_VAR}")

        # If you want to save files in a shared storage, to be used by other Pieces,
        # you should save them under self.results_path
        msg = "This is a text to be saved in a shared storage, to be read by other Pieces!"
        file_path = str(Path(self.results_path)/"msg.txt")
        with open(file_path, "w") as f:
            f.write(msg)

        # If you want to display results directly in the Domino GUI,
        # you should set the attribute self.display_result
        self.display_result = {
            "file_type": "txt",
            "file_path": file_path
        }

        # You should return the results using the Output model
        return OutputModel(
            out_argument_1="a string result",
            out_file_path=file_path
        )