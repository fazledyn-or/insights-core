from falafel.core.plugins import mapper
from falafel.mappers import get_active_lines
from falafel.core import MapperOutput


@mapper("cobbler_modules.conf")
class CobblerModulesConf(MapperOutput):

    @staticmethod
    def parse_content(content):
        """
        Parses cobbler/modules.conf and returns a dict.
        - {
            "authentication": {"module":"authn_spacewalk"},
            "authorization": {"module":"authz_allowall"}
          }
        """
        modules_dict = {}
        section_dict = {}
        for line in get_active_lines(content):
            if line.startswith("["):
                # new section beginning
                section_dict = {}
                modules_dict[line[1:-1]] = section_dict
            elif '=' in line:
                key, _, value = line.partition("=")
                section_dict[key.strip()] = value.strip()
        return modules_dict
