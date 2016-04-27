#|/bin/bash
cd ..
cd ..
cd ..
../../bin/i18ndude rebuild-pot --pot genweb/simpleforum/locales/genweb.simpleforum.pot --create genweb.simpleforum .
cd genweb/simpleforum/locales/ca/LC_MESSAGES
../../../../../../../bin/i18ndude sync --pot ../../genweb.simpleforum.pot genweb.simpleforum.po
cd ..
cd ..
cd en
cd LC_MESSAGES
../../../../../../../bin/i18ndude sync --pot ../../genweb.simpleforum.pot genweb.simpleforum.po
cd ..
cd ..
cd es
cd LC_MESSAGES
../../../../../../../bin/i18ndude sync --pot ../../genweb.simpleforum.pot genweb.simpleforum.po
