# Module 7: Hallucination Testing

This activity intentionally tested whether GitHub Copilot would accept believable but false Pygame API assumptions.

Three attempts used invented or incorrect API details:

1. A nonexistent `Sprite.on_collision()` method.
2. A nonexistent `on_collision` callback parameter for `spritecollide()`.
3. A nonexistent `pygame.sprite.spritebounce()` function.

Copilot rejected the false assumptions rather than hallucinating the requested APIs. The activity still demonstrated why exact library versions, documentation checks, runtime testing, and explicit instructions not to invent undocumented functions are useful safeguards.

## Artifacts

- `Reflection.txt` - Corrected final activity reflection.
- `Copilot_Chat.json` - Exported Copilot conversation from the hallucination-testing activity.
