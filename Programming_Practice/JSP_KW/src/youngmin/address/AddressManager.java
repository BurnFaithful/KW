package youngmin.address;

import java.util.ArrayList;
import java.util.List;

public class AddressManager
{
    private List<AddressBean> address = new ArrayList<AddressBean>();

    public List<AddressBean> getAddress() {
        return address;
    }

    public void Add(AddressBean addAddress)
    {
        address.add(addAddress);
    }

    public void Clear()
    {
        address.clear();
    }
}
