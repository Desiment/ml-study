from categories import Categories


class Tree:
    THRESHOLD = 10
    MAIN_SUBJECT_THRESHOLD = 0.6
    MIDDLE_SUBJECT_THRESHOLD = 0.3
    EPS = 0.1

    def __init__(self):
        pass

    def make_decision(self, entity):

        global_sum = sum(entity)
        entity = [cnt / global_sum for cnt in entity]

        if global_sum < self.THRESHOLD or entity[-1] > 0.5:
            return Categories.UNDEFINED

        top = sorted(entity, reverse=True)
#        print(top)
        if abs(top[0] - top[1]) < self.EPS:
            return Categories.MULTI_SCIENCE

        #Покекаем хуле
        if entity[Categories.TECH_SCIENCE] > self.MAIN_SUBJECT_THRESHOLD:
            return Categories.TECH_SCIENCE
        elif entity[Categories.TECH_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
            if entity[Categories.NATURAL_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                return Categories.MULTI_SCIENCE
            elif entity[Categories.SOCIETY_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                return Categories.MULTI_SCIENCE
            elif entity[Categories.LANGUAGE_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                return Categories.MULTI_SCIENCE
            elif entity[Categories.HUMANITARIAN_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                return Categories.MULTI_SCIENCE
            elif entity[Categories.OTHER_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                return Categories.MULTI_SCIENCE
            else:
                return Categories.TECH_SCIENCE
        else:
            if entity[Categories.NATURAL_SCIENCE] > self.MAIN_SUBJECT_THRESHOLD:
                return Categories.NATURAL_SCIENCE
            elif entity[Categories.NATURAL_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                if entity[Categories.SOCIETY_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                    return Categories.MULTI_SCIENCE
                elif entity[Categories.LANGUAGE_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                    return Categories.MULTI_SCIENCE
                elif entity[Categories.HUMANITARIAN_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                    return Categories.MULTI_SCIENCE
                elif entity[Categories.OTHER_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                    return Categories.MULTI_SCIENCE
                else:
                    return Categories.NATURAL_SCIENCE
            else:
                if entity[Categories.SOCIETY_SCIENCE] > self.MAIN_SUBJECT_THRESHOLD:
                    return Categories.SOCIETY_SCIENCE
                elif entity[Categories.SOCIETY_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                    if entity[Categories.LANGUAGE_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                        return Categories.MULTI_SCIENCE
                    elif entity[Categories.HUMANITARIAN_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                        return Categories.MULTI_SCIENCE
                    elif entity[Categories.OTHER_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                        return Categories.MULTI_SCIENCE
                    else:
                        return Categories.SOCIETY_SCIENCE
                else:
                    if entity[Categories.LANGUAGE_SCIENCE] > self.MAIN_SUBJECT_THRESHOLD:
                        return Categories.LANGUAGE_SCIENCE
                    elif entity[Categories.LANGUAGE_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                        if entity[Categories.HUMANITARIAN_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                            return Categories.MULTI_SCIENCE
                        elif entity[Categories.OTHER_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                            return Categories.MULTI_SCIENCE
                        else:
                            return Categories.LANGUAGE_SCIENCE
                    else:
                        if entity[Categories.HUMANITARIAN_SCIENCE] > self.MAIN_SUBJECT_THRESHOLD:
                            return Categories.HUMANITARIAN_SCIENCE
                        elif entity[Categories.HUMANITARIAN_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                            if entity[Categories.OTHER_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                                return Categories.MULTI_SCIENCE
                            else:
                                return Categories.HUMANITARIAN_SCIENCE
                        else:
                            if entity[Categories.OTHER_SCIENCE] > self.MAIN_SUBJECT_THRESHOLD:
                                return Categories.OTHER_SCIENCE
                            elif entity[Categories.OTHER_SCIENCE] > self.MIDDLE_SUBJECT_THRESHOLD:
                                return Categories.OTHER_SCIENCE
                            else:
                                return Categories.UNDEFINED



