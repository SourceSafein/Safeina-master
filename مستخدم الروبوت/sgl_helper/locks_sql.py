from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr









def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

iqvois1 = "userbot/helpers/styles/Voic/يستاا ولا يهزك حاجهogg"
iqvois2 = "userbot/helpers/styles/Voic/استمر نحن معك.ogg"
iqvois3 = "userbot/helpers/styles/Voic/اديلو واحده ف وشوه.ogg"
iqvois4 = "userbot/helpers/styles/Voic/ياعم اقعد وماتصدعناش.ogg"
iqvois5 = "userbot/helpers/styles/Voic/اللهم لا شماته.ogg"
iqvois6 = "userbot/helpers/styles/Voic/طلع دينه.ogg"
iqvois7 = "userbot/helpers/styles/Voic/امشي بالله يسطا.ogg"
iqvois8 = "userbot/helpers/styles/Voic/انت اسكت انت اسكت.ogg"
iqvois9 = "userbot/helpers/styles/Voic/انت سايق معزه.ogg"
iqvois10 = "userbot/helpers/styles/Voic/وه وه وه.ogg"
iqvois11 = "userbot/helpers/styles/Voic/برافو عليك .ogg"
iqvois12 = "userbot/helpers/styles/Voic/بلوك محترم.ogg"
iqvois13 = "userbot/helpers/styles/Voic/بووم في منتصف الجبهة.ogg"
iqvois14 = "userbot/helpers/styles/Voic/بيتش.ogg"
iqvois15 = "userbot/helpers/styles/Voic/تخوني ؟.ogg"
iqvois15 = "userbot/helpers/styles/Voic/اهه مش عجبك.ogg"
iqvois17 = "userbot/helpers/styles/Voic/تعبان اوي.ogg"
iqvois18 = "userbot/helpers/styles/Voic/انت بتكدب يسطا.ogg"
iqvois19 = "userbot/helpers/styles/Voic/حسبي الله.ogg"
iqvois20 = "userbot/helpers/styles/Voic/هلاس.ogg"
iqvois21 = "userbot/helpers/styles/Voic/زفتت.ogg"
iqvois22 = "userbot/helpers/styles/Voic/خاص.ogg"
iqvois23 = "userbot/helpers/styles/Voic/اي يجدعااان روحو نااامو.ogg"
iqvois24 = "userbot/helpers/styles/Voic/سيبهالك وماشي يعم.ogg"
iqvois25 = "userbot/helpers/styles/Voic/خلاصاانه.ogg"
iqvois26 = "userbot/helpers/styles/Voic/صيااح.ogg"
iqvois27 = "userbot/helpers/styles/Voic/سلاموو عليكوو.ogg"
iqvois28 = "userbot/helpers/styles/Voic/ماالك يابرو.ogg"
iqvois29 = "userbot/helpers/styles/Voic/ناا شوفت نااس مدورهاا.ogg"
iqvois30 = "userbot/helpers/styles/Voic/فيين،.ogg"
iqvois31 = "userbot/helpers/styles/Voic/صبح يابرو.ogg"
iqvois32 = "userbot/helpers/styles/Voic/شويه سكوت.ogg"
iqvois33 = "userbot/helpers/styles/Voic/ضحكة عمر اديب.ogg"
iqvois34 = "userbot/helpers/styles/Voic/طماطه.ogg"
iqvois35 = "userbot/helpers/styles/Voic/انت نيتك كده.ogg"
iqvois36 = "userbot/helpers/styles/Voic/استغفر الله.ogg"
iqvois37 = "userbot/helpers/styles/Voic/روقاان.ogg"
iqvois38 = "userbot/helpers/styles/Voic/متقعدش تحور.ogg"
iqvois39 = "userbot/helpers/styles/Voic/هييي حفله.ogg"
iqvois40 = "userbot/helpers/styles/Voic/لا مستحيل.ogg"
iqvois41 = "userbot/helpers/styles/Voic/لا ولله انت كده روش.ogg"
iqvois42 = "userbot/helpers/styles/Voic/ليه.ogg"
iqvois43 = "userbot/helpers/styles/Voic/خدي قلبي يستاا.ogg"
iqvois44 = "userbot/helpers/styles/Voic/ما بشربش.ogg"
iqvois45 = "userbot/helpers/styles/Voic/مع الاسف.ogg"
iqvois46 = "userbot/helpers/styles/Voic/ع قدي.ogg"
iqvois47 = "userbot/helpers/styles/Voic/من بعدكم.ogg"
iqvois48 = "userbot/helpers/styles/Voic/انت مين.ogg"
iqvois49 = "userbot/helpers/styles/Voic/منورني.ogg"
iqvois50 = "userbot/helpers/styles/Voic/هتلاقيه في الدور الثاني.ogg"
iqvois51 = "userbot/helpers/styles/Voic/نستودعكم الله.ogg"
iqvois52 = "userbot/helpers/styles/Voic/هه ظريف.ogg"
iqvois53 = "userbot/helpers/styles/Voic/ههاي مفكرش احطها.ogg"
iqvois54 = "userbot/helpers/styles/Voic/فينهم.ogg"
iqvois55 = "userbot/helpers/styles/Voic/مافيش مخ.ogg"
iqvois56 = "userbot/helpers/styles/Voic/عاوز انام.ogg"
iqvois57 = "userbot/helpers/styles/Voic/افتحك فتح.ogg"
iqvois58 = "userbot/helpers/styles/Voic/وه مالك.ogg"
iqvois59 = "userbot/helpers/styles/Voic/اي يابرنس مالك.ogg"
iqvois60 = "userbot/helpers/styles/Voic/زهقان.ogg"
iqvois61 = "userbot/helpers/styles/Voic/زهقان للصبح.ogg"
iqvois62 = "userbot/helpers/styles/Voic/زهقان للسنه الجاايه.ogg"
iqvois63 = "userbot/helpers/styles/Voic/حشو عيالكم.ogg"
iqvois64 = "userbot/helpers/styles/Voic/هموتهم.ogg"
iqvois65 = "userbot/helpers/styles/Voic/تخ تخ .ogg"
iqvois66 = "userbot/helpers/styles/Voic/سرسجي.ogg"
iqvois67 = "userbot/helpers/styles/Voic/ناا مشغول.ogg"
iqvois68 = "userbot/helpers/styles/Voic/خلصت امسك سلك عريان.ogg"
iqvois69 = "userbot/helpers/styles/Voic/اوعاا تخاف.ogg"
iqvois70 = "userbot/helpers/styles/Voic/عسول.ogg"
iqvois71 = "userbot/helpers/styles/Voic/انا هوريك.ogg"
iqvois72 = "userbot/helpers/styles/Voic/ابو ام الهزار.ogg"
iqvois73 = "userbot/helpers/styles/Voic/انت مالك.ogg"
iqvois74 = "userbot/helpers/styles/Voic/انا ماشي هخرج.ogg"
iqvois75 = "userbot/helpers/styles/Voic/قدك وقد بلدك.ogg"
iqvois76 = "userbot/helpers/styles/Voic/خلااااص.ogg"
iqvois77 = "userbot/helpers/styles/Voic/اهدي يابرو.ogg"
iqvois78 = "userbot/helpers/styles/Voic/انت لسه بتتكلم.ogg"
iqvois79 = "userbot/helpers/styles/Voic/مش قولتك رجعني.ogg"
iqvois80 = "userbot/helpers/styles/Voic/ماقبوله منك.ogg"
iqvois81 = "userbot/helpers/styles/Voic/ليه كده.ogg"
iqvois82 = "userbot/helpers/styles/Voic/اوك.ogg"
iqvois83 = "userbot/helpers/styles/Voic/ينعل كده.ogg"
iqvois84 = "userbot/helpers/styles/Voic/مالك يسطا انا هناogg"
iqvois85 = "userbot/helpers/styles/Voic/عملت ايه.ogg"
iqvois86 = "userbot/helpers/styles/Voic/مالك ياوش البرس.ogg"
iqvois87 = "userbot/helpers/styles/Voic/ييييييي.ogg"
iqvois88 = "userbot/helpers/styles/Voic/مقريق.ogg"
iqvois89 = "userbot/helpers/styles/Voic/عالم تعبانه.ogg"
iqvois90 = "userbot/helpers/styles/Voic/ياخي اسكت اسكت.ogg"
iqvois91 = "userbot/helpers/styles/Voic/هما فين.ogg"
iqvois92 = "userbot/helpers/styles/Voic/خلصانه ياعم.ogg"
iqvois93 = "userbot/helpers/styles/Voic/هو.ogg"
iqvois94 = "userbot/helpers/styles/Voic/مابفكرش اغيرها.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
