from typing import Optional, List

from pydantic import BaseModel


class Mora(BaseModel):
    text: str
    consonant: Optional[str]
    consonant_length: Optional[float]
    vowel: str
    vowel_length: float
    pitch: float


class AccentPhrase(BaseModel):
    moras: List[Mora]
    accent: int
    pause_mora: Optional[Mora]
    is_interrogative: bool


class AudioQuery(BaseModel):
    accent_phrases: List[AccentPhrase]
    speedScale: float
    pitchScale: float
    intonationScale: float
    volumeScale: float
    prePhonemeLength: float
    postPhonemeLength: float
    outputSamplingRate: int
    outputStereo: bool
    kana: Optional[str]
