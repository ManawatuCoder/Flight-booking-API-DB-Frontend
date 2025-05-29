import{defineStore} from "pinia";
import{ref} from "vue";
export const useSuccessStatusStore = defineStore("layout", () => {
    const successStatus = ref(false);
    const isBookingRef = ref(false);
    const setSuccessStatus = (isSuccess) => {
        successStatus.value = isSuccess;
    }
    const setBookingRef = (isBooking) => {
        isBookingRef.value = isBooking;
    }
    return {setSuccessStatus, successStatus, isBookingRef, setBookingRef};
})