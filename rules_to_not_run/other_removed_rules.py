        {
            "name": "That / Which",
            "re": [
                "\\w+ \\w+ which",
                "\\w+ \\w+ that"
            ]
        },
        {
            "name": "Between / Among",
            "re": "(between|among)"
        },
        {
            "name": "Fewer / Less",
            "re": "(fewer|less)"
        },

        {
            "name": "For more, less/fewer, better, worse",
            "suffix": "",
            "re": [
                "increase", "decrease"
            ]
        },

        {
            "comments": [
                "Do not use the apostrophe when creating plurals (i.e., Joneses, not Jones's).",
                "Use ' s after singular nouns and indefinite pronouns that do not end and after plural nouns that do not end in s."
            ],
            "re": "\\w+'s"
        },

                {
                    "name": "No space before parentheses",
                    "re": "\\w\\("
                },

        {
            "name": "Dashes",
            "prefix": "\\w",
            "suffix": "\\w",
            "re": [
                    "---",
                    " --- ",
                    " ---",
                    "--- "
            ]
        },
