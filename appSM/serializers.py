from datetime import datetime
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    def to_internal_value(self, data):
         
        """
        Valida o formato esperado onde as chaves são datas 'DD/MM/YYYY' 
        e os valores são float ou null.
        """
        if not isinstance(data, dict):
            raise serializers.ValidationError("Os dados devem ser um dicionário.")
        
        for key, value in data.items():
            # Valida a chave como uma data no formato 'DD/MM/YYYY'
            try:
                datetime.strptime(key, '%d/%m/%Y')
            except ValueError:
                raise serializers.ValidationError(f"A chave '{key}' não está no formato DD/MM/YYYY.")
            
            # Valida que o valor seja float ou None
            if value is not None and not isinstance(value, (float, int)):
                raise serializers.ValidationError(f"O valor para a chave '{key}' deve ser um número ou null.")
        
        return super().to_internal_value(data)
        
 