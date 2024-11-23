import os


class Config(object):
    API_HASH = os.environ.get("3dc29da97738fe42da9e8f2524169a9c")
    BOT_TOKEN = os.environ.get("7650487749:AAGVPsNpW9Ho_5XCRYDFsToeaLnWKwsTj4s")
    TELEGRAM_API = os.environ.get("28789183")
    OWNER = os.environ.get("6434831584")
    OWNER_USERNAME = os.environ.get("@TK_Mob_TY")
    PASSWORD = os.environ.get("BNF")
    DATABASE_URL = os.environ.get("mongodb+srv://bharathkalladi38:4TDnaR1dZqAEshQq@cluster0.ps5ucul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002272062522")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("BQCyNwMApuQZqxG2UtCVG1buL2Y5LTfaUDDJQx13612uQLg5ooN_sXNsbe6HV9puf4Ae-ymPPpoiTetLDzSmOAsJYzXLfTUks0GDOW0z3f0G2pNyQvldhuftO9hw4f0rF50RrTuP0PdINZFTT4f6L_UGkVIJ1yRgn_QWt3IEmYy5S28Yu_ED_19jilDyV1aG41oRByrlk0ZWi3OwLHU7C_PfT_m1fKlaQrmWcR-3QbLLvxm-kq4FaMD2eZGikK7CAV4-XtKtIkRzlmU1q3YsZjAKK6yTddfDxXLEMvJgzkXsHzkyyoorTxemV9Fh4BfuOJ3rf8y2P6DRXU_ilVc4UO9LOVWJugAAAAFxMeNwAA", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
