"""IFBench - Generalizing Verifiable Instruction Following."""

__version__ = "1.0.0"
__author__ = "Allen Institute for AI"

# Import main evaluation functions
try:
    from . import evaluation_lib
    from . import instructions
    from . import instructions_registry
    from . import instructions_util
    
    # Make key classes and functions available at package level
    from .evaluation_lib import (
        InputExample,
        OutputExample,
        read_prompt_list,
        read_prompt_to_response_dict,
        test_instruction_following_strict,
        test_instruction_following_loose,
        write_outputs,
        print_report,
    )
    
    __all__ = [
        'evaluation_lib',
        'instructions',
        'instructions_registry', 
        'instructions_util',
        'InputExample',
        'OutputExample',
        'read_prompt_list',
        'read_prompt_to_response_dict',
        'test_instruction_following_strict',
        'test_instruction_following_loose',
        'write_outputs',
        'print_report',
    ]
    
except ImportError:
    # Fallback for direct script usage
    pass