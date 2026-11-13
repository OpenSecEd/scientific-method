#!/bin/sh
# Regenerate the hit-list table and the CSV export of one session.
# Usage: export.sh <effect|attribution|sufficient|necessary|method> <outdir>
s=$1; O=$2
case $s in
effect) scholar sessions export mfa-effect -f table --bearing-only --lang en --label hits-effect --track "Effect of multi-factor authentication" --theme measured-effect="Measurement of effect" --theme bypass-attack="Bypass or attack on MFA" --theme effect-review="Systematic review of effect" -o $O/mfa-effect-full ;;
attribution) scholar sessions export mfa-attribution -f table --bearing-only --lang en --label hits-attribution --track "What each factor contributes" --theme local-malware="Local attacks and malware" --theme key-resists-remote="A key resists remote attacks" --theme fallback-recovery="Fallback and recovery" --theme synced-passkeys="Synced passkeys" --theme second-factor-weakness="Weak second factors" --theme formal-analysis="Formal analysis" -o $O/mfa-attribution-full ;;
sufficient) scholar sessions export mfa-sufficient -f table --bearing-only --lang en --label hits-sufficient --track "Is multi-factor authentication sufficient" --theme aitm="Phishing proxies and session theft" --theme recovery="Recovery and fallback" --theme fidoatk="Attacks on FIDO2 and passkeys" --theme analysis="Formal and analytical security analyses" -o $O/mfa-sufficient-full ;;
necessary) scholar sessions export mfa-necessary -f table --bearing-only --lang en --label hits-necessary --track "Is multi-factor authentication necessary" --theme RBA="Risk-based authentication" --theme FIDO="Cryptographic keys and passkeys" --theme REC="Account recovery and fallback" --theme STD="Standards and requirements" --theme ATT="Attacks on and measurements of MFA" -o $O/mfa-necessary-full ;;
esac
scholar sessions export mfa-$s -f csv -o $O/mfa-$s
