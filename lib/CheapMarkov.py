from random import randint

class CheapMarkov:
    def generate_text_from_array(self, inputarray, textlength = 100, look_forward = 4):
        self.table = self.populate_table_from_array(inputarray, look_forward)
        return self.gen_text(textlength, self.table, look_forward)

    def populate_table_from_string(self, inputstring, look_forward = 4):
        table = {}
        for i in range (0, len(inputstring)):
            part = inputstring[i : (i + look_forward)]
            if part not in table:
                table[part] = {}
        for i in range(0, (len(table) - look_forward)):
            part_index = inputstring[i : (i + look_forward)]
            part_count = inputstring[(i + look_forward) : (i + look_forward + look_forward)]
            if part_count not in table[part_index]:
                table[part_index][part_count] = 1
            else:
                table[part_index][part_count] += 1
        return table

    def populate_table_from_array(self, inputarray, look_forward = 4):
        table = {}
        for i in range(0, len(inputarray)):
            subtable = self.populate_table_from_string(inputarray[i], look_forward)
            table.update(subtable)
        return table

    def get_weighted_part(self, part):
        if not part:
            return None

        total = len(part.keys())
        rando = randint(1, total)
        for key in part:
            if rando <= part[key]:
                return key
            else:
                rando -= part[key]

    def gen_text(self, length, table, look_forward = 4):
        all_parts = table.keys()
        rand_idx = randint(0, len(all_parts))
        part = all_parts[rand_idx]
        output = part

        for i in range (0, (length / look_forward)):
            new_part = self.get_weighted_part(table[part])
            if new_part:
                part = new_part
                output += new_part
            else:
                rand_idx = randint(0, len(all_parts))
                part = all_parts[rand_idx]
        return output

    def get_num_fragments(self):
        if self.table:
            return len(self.table)
        else:
            return 0
