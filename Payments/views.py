class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Payment.objects.filter(status='in-progress')
    def perform_create(self, serializer):
        serializer.save()





