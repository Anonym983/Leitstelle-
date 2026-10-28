from pathlib import Path
from polizei.logging_setup import setup_logging

def main():
    root=Path(__file__).resolve().parent
    setup_logging(root/"logs")
    try:
        from vorschau_erstellen import build_preview
        build_preview()
    except Exception:
        import logging
        logging.getLogger("polizei.preview").exception("Vorschau konnte nicht aktualisiert werden")
    from polizei import core
    core.bot.run(core.TOKEN,log_handler=None)

if __name__=="__main__":main()
