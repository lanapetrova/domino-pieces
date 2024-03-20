from domino.testing import piece_dry_run

def test_mynewpiece():
    # Define input and secrets data
    input_data = dict(
        in_argument_1=10.5,
        in_argument_2='test string',
        in_argument_3=True,
    )
    secrets_data = dict(
        SECRET_VAR="secret_value"
    )

    # Dry-run the Piece
    piece_output = piece_dry_run(
        piece_name="MyNewPiece",
        input_data=input_data,
        secrets_data=secrets_data
    )

    # Compare the output with the expected output
    assert piece_output["out_argument_1"] == "a string result"
    assert piece_output["out_argument_2"].split("/")[-1] == "msg.txt"